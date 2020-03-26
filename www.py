import datetime
import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("")
app_f = firebase_admin.initialize_app(cred)

message = messaging.Message(
    notification=messaging.Notification(
        title="213",
        body="921",
        image="",
    ),
    data={
        'url': "",
    },

    android=messaging.AndroidConfig(
        # collapse_key=,
        priority='high',
        ttl=datetime.timedelta(hours=6),
        # data={},
        notification=messaging.AndroidNotification(color='#1c2676'),
        # for analyzing on all platforms and link on web. https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages
        # fcm_options={},
    ),

    # apns' config is more complicated than android's. So, I only listed useful options here and please refer Apple docs for more detail.
    apns=messaging.APNSConfig(
        headers={
            # "apns-collapse-id": "qqq",
            # TODO to fit Ruby form
            # "apns-expiration": "1585190586",
            # "apns-priority": "10", # default
                 },
        payload=messaging.APNSPayload(
            aps=messaging.Aps(
                # override notification field
                # alert=messaging.ApsAlert(
                #     title='111',
                #     subtitle="222",
                #     body='333',
                # ),
                # badge=42,
                sound="default",
                # for ios native programming?
                # thread_id="", category="",
                # To perform a silent background update, specify the value 1 and don't include the alert, badge, or sound keys in your payload.
                # content_available=1,
                # Notification service app extensions only operate on remote notifications that are configured to display an alert to the user. If alerts are disabled for your app, or if the payload specifies only the playing of a sound or the badging of an icon, the extension is not employed.
                mutable_content=1,
            ),
            # override data field and seems accept any data type
            # xxx=10,
            # url="xxx",
        ),
        # fcm_options={},
    ),

    # token="",
    # topic='android',
    # topic='ios',
    # condition="'ios' in topics",
    condition="'android' in topics",
    # condition="'ios' in topics || 'android' in topics",
)

response = messaging.send(message)
print('Successfully sent message:', response)

