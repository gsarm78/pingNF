# This NF is a simple Ping NF towards an IP ADDRESS AND PORT NUMBER
# USE: http://127.0.0.1:5000/ping?ip=8.8.8.8&port=80
# Implements GET method of HTTP, to retrieve the Ping results


from flask import Flask, request, jsonify
import subprocess
import platform

app = Flask(__name__)

def perform_ping(host, count=4):
    """Function to perform the ping operation."""
    # Building the ping command based on the platform
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), host]

    try:
        output = subprocess.check_output(command).decode()
        return True, output
    except subprocess.CalledProcessError:
        return False, ""

@app.route('/ping', methods=['GET'])
def ping():
    """API endpoint to perform ping."""
    ip_address = request.args.get('ip')
    port = request.args.get('port', 80)  # Default port is 80

    success, response = perform_ping(ip_address)
    return jsonify({
        'ip': ip_address,
        'port': port,
        'success': success,
        'response': response
    })

if __name__ == '__main__':
    app.run(debug=True)
