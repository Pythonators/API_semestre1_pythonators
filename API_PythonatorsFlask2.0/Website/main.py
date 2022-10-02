<<<<<<< HEAD
from flask import Flask

from Website import create_app

app = create_app()

#app = Flask(__name__)
if __name__ == '__main__':
=======
from flask import Flask

from Website import create_app

app = create_app()

#app = Flask(__name__)
if __name__ == '__main__':
>>>>>>> 6165261cd08a060cae6648c8024d20a8d333b3dc
    app.run(debug=True)