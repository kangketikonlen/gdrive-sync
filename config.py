# Set scopes and credentials for Google APIs
SCOPES = [
    'https://www.googleapis.com/auth/drive.metadata.readonly',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive Sync'
# Set path to the uploaded folder is located
FULL_PATH = r'/Users/kangketik/Database'
DIR_NAME = 'Database'
# Set Mime type for uploaded folder
GOOGLE_MIME_TYPES = {
    'application/vnd.google-apps.document':
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.google-apps.spreadsheet':
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.google-apps.presentation':
        'application/vnd.openxmlformats-officedocument.presentationml.presentation'
}
# Set excluded files
EXCLUDED_FILES = [
    ".DS_Store"
]