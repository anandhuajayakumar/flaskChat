from modules import createApp

(socketio, app) = createApp()

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0")
