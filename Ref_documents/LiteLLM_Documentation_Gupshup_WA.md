# Send messages

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 🚧  The API will not work if called from any client(UI - AJAX, JS HTTP, etc) directly.

Using this API you can send different types of messages to users. The different types of message objects are described here.

## Message object description for different `types` of messages   [Skip link to Message object description for different ](https://docs.gupshup.io/reference/msg\#message-object-description-for-different-types-of-messages)

### Text message   [Skip link to Text message](https://docs.gupshup.io/reference/msg\#text-message)

text message object

```rdmd-code lang-json theme-light

{
   "type":"text",
   "text":"Hello user, how are you?"
}

```

| Key | Type | Description | Sample |
| --- | --- | --- | --- |
| `text` | string | **Required**<br>The text message that will be sent to the user. | Hello user, how are you? |

### Image message   [Skip link to Image message](https://docs.gupshup.io/reference/msg\#image-message)

image message object

```rdmd-code lang-json theme-light

{
   "type":"image",
   "originalUrl":"https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg",
   "previewUrl":"https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg",
   "caption":"Sample image"
}

```

| Key | Type | Description | Sample |
| --- | --- | --- | --- |
| `originalUrl` | string | Public URL of the image hosted. | [https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg](https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg) |
| `previewUrl` | string | Public URL of the thumbnail of the image. | [https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg](https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg) |
| `caption` | string | **Optional**<br>Caption of the image | Sample image |

### File message   [Skip link to File message](https://docs.gupshup.io/reference/msg\#file-message)

file message object

```rdmd-code lang-json theme-light

{
   "type":"file",
   "url":"https://www.buildquickbots.com/whatsapp/media/sample/pdf/sample01.pdf",
   "filename":"Sample file"
}

```

| Key | Type | Description | Sample |
| --- | --- | --- | --- |
| `url` | string | Public URL of the file hosted | [https://www.buildquickbots.com/whatsapp/media/sample/pdf/sample01.pdf](https://www.buildquickbots.com/whatsapp/media/sample/pdf/sample01.pdf) |
| filename | string | Name of the file | Sample file |

### Audio message   [Skip link to Audio message](https://docs.gupshup.io/reference/msg\#audio-message)

audio message object

```rdmd-code lang-json theme-light

{
   "type":"audio",
   "url":"https://www.buildquickbots.com/whatsapp/media/sample/audio/sample02.mp3"
}

```

| Key | Type | Description | Sample |
| --- | --- | --- | --- |
| `url` | string | Public URL of the audio file. | [https://www.buildquickbots.com/whatsapp/media/sample/audio/sample02.mp3](https://www.buildquickbots.com/whatsapp/media/sample/audio/sample02.mp3) |

### Video message   [Skip link to Video message](https://docs.gupshup.io/reference/msg\#video-message)

video message object

```rdmd-code lang-json theme-light

{
   "type":"video",
   "url":"https://www.buildquickbots.com/whatsapp/media/sample/video/sample01.mp4"
}

```

| Key | Type | Description | Sample |
| --- | --- | --- | --- |
| `url` | string | Public URL of the video file. | [https://www.buildquickbots.com/whatsapp/media/sample/video/sample01.mp4](https://www.buildquickbots.com/whatsapp/media/sample/video/sample01.mp4) |
| `caption` | string | **Optional**<br>Caption of the video | Sample caption |

### Sticker message   [Skip link to Sticker message](https://docs.gupshup.io/reference/msg\#sticker-message)

sticker message object

```rdmd-code lang-json theme-light

{
   "type":"sticker",
   "url":"http://www.buildquickbots.com/whatsapp/stickers/SampleSticker01.webp"
}

```

| Key | Type | Description | Sample |
| --- | --- | --- | --- |
| `url` | string | Public URL of the sticker file. | [http://www.buildquickbots.com/whatsapp/stickers/SampleSticker01.webp](http://www.buildquickbots.com/whatsapp/stickers/SampleSticker01.webp) |

### Interactive - List message   [Skip link to Interactive - List message](https://docs.gupshup.io/reference/msg\#interactive---list-message)

list message object

```rdmd-code lang-json theme-light

{
   "type":"list",
   "title":"title text",
   "body":"body text",
   "footer":"footer text",
   "msgid":"list1",
   "globalButtons":[\
      {\
         "type":"text",\
         "title":"Global button"\
      }\
   ],
   "items":[\
      {\
         "title":"first Section",\
         "subtitle":"first Subtitle",\
         "options":[\
            {\
               "type":"text",\
               "title":"section 1 row 1",\
               "description":"first row of first section description",\
               "postbackText":"section 1 row 1 postback payload"\
            },\
            {\
               "type":"text",\
               "title":"section 1 row 2",\
               "description":"second row of first section description",\
               "postbackText":"section 1 row 2 postback payload"\
            },\
            {\
               "type":"text",\
               "title":"section 1 row 3",\
               "description":"third row of first section description",\
               "postbackText":"section 1 row 3 postback payload"\
            }\
         ]\
      },\
      {\
         "title":"second section",\
         "subtitle":"second Subtitle",\
         "options":[\
            {\
               "type":"text",\
               "title":"section 2 row 1",\
               "description":"first row of second section description",\
               "postbackText":"section 1 row 3 postback payload"\
            }\
         ]\
      }\
   ]
}

```

| Key | Type | Description | Note |
| --- | --- | --- | --- |
| `title` | string | The title/header text for the list message | \- Maximum characters: 60.<br>\- Formatting allows emojis, but not markdown. |
| `body` | string | The body text for the list message | \- Maximum characters: 1024<br>\- Emojis and markdown are supported. Links are supported. |
| `msgid` | string | **Optional**<br>It's a developer-defined message-id for a specific list message. The inbound message-event payload consists of this id when the user replies to a list message. It's a feature provided by our platform, and it helps developers set the context of a reply for use-cases like chatbots. |  |
| `globalButtons` | array | See [globalButtons array description](https://docs.gupshup.io/reference/msg#globalbuttons-array-description) |  |
| `items` | array | See [items array description](https://docs.gupshup.io/reference/msg#items-array-description) | Up to 10 items supported. |
| `footer` | string | The footer text for the list message. | \- Maximum characters: 60 |

##### `globalButtons` array description   [Skip link to [object Object]](https://docs.gupshup.io/reference/msg\#globalbuttons-array-description)

| Key | Type | Description | Note |
| --- | --- | --- | --- |
| `type` | string | Only `text` is supported as the title of the Global button | \- Must always be `text` |
| `title` | string | The title of the global button | \- It cannot be an empty string and must be unique within the message. - Maximum of 20 characters. - Does not allow emojis or markdown. |

##### `items` array description   [Skip link to [object Object]](https://docs.gupshup.io/reference/msg\#items-array-description)

| Key | Type | Description | Note |
| --- | --- | --- | --- |
| `title` | string | The title of a section in the list message. | \- Maximum characters: 24<br>\- Required if the message has more than one section. |
| `options` | array | Contains list of items in a section.<br>See [options array description](https://docs.gupshup.io/reference/msg#options-array-description). |  |

##### `options` array description   [Skip link to [object Object]](https://docs.gupshup.io/reference/msg\#options-array-description)

| Key | Type | Description | Note |
| --- | --- | --- | --- |
| `type` | string | Only text is supported |  |
| `title` | string | The title of the item in the list. | Maximum characters: 24 |
| `description` | string | **Optional**<br>The description of the item in the list. | Maximum characters: 72 |
| `postbackText` | string | **Optional**<br>A custom payload you can configure to receive when the user selects a particular item in the list. |  |

### Interactive - Quick reply message   [Skip link to Interactive - Quick reply message](https://docs.gupshup.io/reference/msg\#interactive---quick-reply-message)

textimagevideofile

```rdmd-code lang-json theme-light

{
   "type":"quick_reply",
   "msgid":"qr1",
   "content":{
      "type":"text",
      "header":"this is the header",
      "text":"this is the body",
      "caption":"this is the footer"
   },
   "options":[\
      {\
         "type":"text",\
         "title":"First",\
         "postbackText": "dev-defined-postback1"\
      },\
      {\
         "type":"text",\
         "title":"Second",\
         "postbackText": "dev-defined-postback2"\
      },\
      {\
         "type":"text",\
         "title":"Third",\
         "postbackText": "dev-defined-postback3"\
      }\
   ]
}

```

```rdmd-code lang-json theme-light

{
   "type":"quick_reply",
   "msgid":"qr1",
   "content":{
      "type":"image",
      "url":"https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg",
      "text":"this is the body",
      "caption":"this is the footer"
   },
   "options":[\
      {\
         "type":"text",\
         "title":"First",\
         "postbackText": "dev-defined-postback1"\
      },\
      {\
         "type":"text",\
         "title":"Second",\
         "postbackText": "dev-defined-postback2"\
      },\
      {\
         "type":"text",\
         "title":"Third",\
         "postbackText": "dev-defined-postback3"\
      }\
   ]
}

```

```rdmd-code lang-json theme-light

{
   "type":"quick_reply",
   "msgid":"qr1",
   "content":{
      "type":"video",
      "url":"https://www.buildquickbots.com/whatsapp/media/sample/video/sample01.mp4",
      "text":"this is the body",
      "caption":"Sample video"
   },
   "options":[\
      {\
         "type":"text",\
         "title":"First",\
         "postbackText": "dev-defined-postback1"\
      },\
      {\
         "type":"text",\
         "title":"Second",\
         "postbackText": "dev-defined-postback2"\
      },\
      {\
         "type":"text",\
         "title":"Third",\
         "postbackText": "dev-defined-postback3"\
      }\
   ]
}

```

```rdmd-code lang-json theme-light

{
   "type":"quick_reply",
   "msgid":"qr1",
   "content":{
      "type":"file",
      "url":"https://www.buildquickbots.com/whatsapp/media/sample/pdf/sample01.pdf",
      "text":"this is the body",
      "filename":"Sample file",
      "caption":"this is the footer"
   },
   "options":[\
      {\
         "type":"text",\
         "title":"First",\
         "postbackText": "dev-defined-postback1"\
      },\
      {\
         "type":"text",\
         "title":"Second",\
         "postbackText": "dev-defined-postback2"\
      },\
      {\
         "type":"text",\
         "title":"Third",\
         "postbackText": "dev-defined-postback3"\
      }\
   ]
}

```

| Key | Type | Description | Note |
| --- | --- | --- | --- |
| `msgid` | string | **Optional**<br>It's a developer-defined message-id for a specific list message. The inbound message-event payload consists of this id when the user replies to a list message. It's a feature provided by our platform, and it helps developers set the context of a reply for use-cases like chatbots. |  |
| `content` | object | See [content object description](https://docs.gupshup.io/reference/msg#content-object-description) |  |
| `options` | array | See [options array description](https://docs.gupshup.io/reference/msg#options-array-description-1) | Up to 3 options are supported. |
|  |  |  |  |

##### `content` object description   [Skip link to [object Object]](https://docs.gupshup.io/reference/msg\#content-object-description)

| Key | Type | Description | Note |
| --- | --- | --- | --- |
| `type` | string | The type of quick reply message. | Supported types: `text`, `image`, `video`, and `document`. |
| `header` | string | **Optional**<br>It is header of the text message. | `Header` is only applicable to a quick reply message of type `text`.<br>Maximum characters: 20 |
| `url` | string | Public URL of the media file. | `url` is only applicable to quick reply messages of type: `image`, `video`, and `file`. |
| `text` | string | It is the body of the message. |  |
| `filename` | string | Name of the file. | `filename` is only applicable to a quick reply message of type: `file`. |
| `caption` | string | **Optional**<br>It is the footer of the message. | Maximum characters: 60 |

##### `options` array description   [Skip link to [object Object]](https://docs.gupshup.io/reference/msg\#options-array-description-1)

| Key | Type | Description | Note |
| --- | --- | --- | --- |
| `type` | string | The type of the button. | Only text type is supported. |
| `title` | string | The title of the button. | It cannot be an empty string and it must be unique within the message.<br>Maximum characters: 20. Does not allow emojis or markdown. |
| `postbackText` | string | Developer-defined payload that will be returned when the button is clicked in addition to the display text on the button. |  |

### Location message   [Skip link to Location message](https://docs.gupshup.io/reference/msg\#location-message)

location message

```rdmd-code lang-json theme-light

{
   "type":"location",
   "longitude":72.877655,
   "latitude":19.075983,
   "name":"Mumbai",
   "address":"Mumbai, Maharashtra"
}

```

### Contact message   [Skip link to Contact message](https://docs.gupshup.io/reference/msg\#contact-message)

contact message

```rdmd-code lang-json theme-light

{
   "type":"contact",
   "contact":{
      "addresses":[\
         {\
            "city":"Menlo Park",\
            "country":"United States",\
            "countryCode":"us",\
            "state":"CA",\
            "street":"1 Hacker Way",\
            "type":"HOME",\
            "zip":"94025"\
         },\
         {\
            "city":"Menlo Park",\
            "country":"United States",\
            "countryCode":"us",\
            "state":"CA",\
            "street":"200 Jefferson Dr",\
            "type":"WORK",\
            "zip":"94025"\
         }\
      ],
      "birthday":"1995-08-18",
      "emails":[\
         {\
            "email":"personal.mail@gupshup.io",\
            "type":"Personal"\
         },\
         {\
            "email":"devsupport@gupshup.io",\
            "type":"Work"\
         }\
      ],
      "name":{
         "firstName":"John",
         "formattedName":"John Wick",
         "lastName":"Wick"
      },
      "org":{
         "company":"Guspshup",
         "department":"Product",
         "title":"Manager"
      },
      "phones":[\
         {\
            "phone":"+1 (940) 555-1234",\
            "type":"HOME"\
         },\
         {\
            "phone":"+1 (650) 555-1234",\
            "type":"WORK",\
            "wa_id":"16505551234"\
         }\
      ],
      "urls":[\
         {\
            "url":"https://www.gupshup.io",\
            "type":"WORK"\
         }\
      ]
   }
}

```

## Supported Content-Types   [Skip link to Supported Content-Types](https://docs.gupshup.io/reference/msg\#supported-content-types)

| Type | Supported Content-Types | Size limit | Note |
| --- | --- | --- | --- |
| **text** | Text content for the message. | Maximum characters supported: 4096. | \- To include a URL preview in the message make sure the URL begins with http:// or https://. - For a URL to be previewed, the hostname is required, IP addresses are not considered. - If a text message has multiple URLs, only the first URL is previewed. |
| **image** | `image/jpeg`, and `image/png` | Maximum file size: 5 MB | WhatsApp vertically crops images with the 1:91:1 aspect ratio: 800×418 pixels. To communicate effectively, design the image such that the crux information is at the center of the image. |
| **file** | Any valid MIME-type | Maximum file size: 100 MB |  |
| **audio** | `audio/aac`, `audio/mp4`, `audio/amr`, `audio/mpeg`, `audio/ogg; codecs=opus`. | Maximum file size: 16 MB | The base audio/ogg type is not supported. |
| **video** | `video/mp4`, `video/3gpp` | Maximum file size: 16 MB | Only H.264 video codec and AAC audio codec is supported. |
| **sticker** | `.webp` | Maximum file size: 100 KB | \- Each sticker has a transparent background. There is no support for sending messages with animated stickers. - Stickers must be exactly 512x512 pixels. |

channel

string

required

The channel for sending messages.

source

int64

required

Registered WhatsApp Business API phone number

destination

int64

required

User's phone number

message

object

required

Text

Image

Document

Video

Sticker

Interactive - List message

Quick reply - text

Quick reply - Image/Video

Quick reply - File

Location message

Contact message

src.name

string

required

The Gupshup app name registered against the phone number provided in the API.

disablePreview

boolean

This is only applicable for text messages. By default, the mobile WhatsApp application recognizes URLs and makes them clickable. To include a URL preview, include "preview\_url": true in the message body and make sure the URL begins with http:// or https://. A hostname is required, IP addresses are not matched.

truefalse

encode

boolean

This flag is used for sending an emoji in an Interactive List message. If the list message consists of emojis, set the encode flag to 'true'. This flag will not affect any other type of message.

truefalse

Content-Type

string

required

application/x-www-form-urlencoded

apikey

string

required

# `` 2XX      Send message API requests received by our platform are processed asynchronously, and hence you will always get an HTTP\_SUCCESS(200 to 299) response range if the API request made is correct.

object

status

string

The API call was successfully made and the request is submitted.

messageId

string

It is the unique identifier for a message. You can track message status via the DLR message events obtained on the webhook.

Updated 10 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

```

xxxxxxxxxx

1curl --request POST \

2     --url https://api.gupshup.io/wa/api/v1/msg \

3     --header 'Content-Type: application/x-www-form-urlencoded' \

4     --header 'accept: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 2XX

Updated 10 months ago

* * *

Did this page help you?

Yes

No

[iframe](javascript:false)

