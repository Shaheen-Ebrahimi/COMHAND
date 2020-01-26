import speech_recognition as sr

def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


    # recognize speech using Google Cloud Speech
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = r'''{
    "type": "service_account",
    "project_id": "comhand",
    "private_key_id": "f3d0c3f359c5d3c21c44bf9c0eac075f090ece28",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCnzexUrqqRaQ4u\nBLYV4ky0qavSZGz3BW0PvzjLtlh6oq8SrWSYNcAR6iWLXe5tW84mcYR7M0jXlqLI\no1gLuJ4VpVVN1+Vtexvs7fytFF4g2rdmydLp54XSR2rWSMeVwUb82AQAesH7uTzG\nNtPj/aMvF9cAbN5VFjBB/V35fdbLTx7qV5Gj3ecT11IvRvJ1x9K7Z4xcUC9oBTuP\n9oll+7ki/4N+AhxYWZr+VAPgH5oIGtYEXNdKiwj+2qwe6pKZBldMHhgyn08Uu4VH\nLcmPlYEICF8YT1xVFM7uTdXloxEofNW2GDDmLFbglIKUx/2CuO0LQlhTtjIg2S88\n8u4kMj2lAgMBAAECggEAF6fxFDMXeq5bwGMLpGQluiZdQajEr8JFEL49bIKFUKyU\nj8Z/8vFI5X2j01TnouUZV9QTACdHspTa1/wnEmfxaU3Ii9PO1TNQyYL3ZxMC/hC3\nYDc9k5n/BJjq19CkyljYABcX4VVs+WawyaS7FF4SXjY3Kiku4sHhBbyJPf3ehQSk\n/lzk+D3n1Ibcx4LOGUkcLaNiEipVv5ia9IyTB1lO4pWS+dtRhAOfsVmSXbPgOZK1\nqKW4E8nMcs7w48Vw1wG4cprDuGFzrz2Ohv9stiGJ+CqGrrOg53xOin3vR2Erx6V9\n0hMFbrzF1fpZ7N1WfFUal+PZ+qoeTLk7Yfcwek2sFQKBgQDSRNPrqe8podgsc0e0\n8BkKYLRelb7ibjrno8j6C/HnP6I0aF6UUIJUPKnbHyfaw0hkUmOL4R4nCpZ8abYd\nvBGabTaMj5st8OtoQU/RjzkOiV/nrDMTXWUdn2dMFEUHDTmIljMpXtQNrZtHk8b/\n52QD+T6VrAhimf6rN9KSMd5drwKBgQDMTMtZW7ErYZLvzZNovsG49Izkv4vJ/7zm\nzT2PPjWmACsyOlg1gU/KEYN8Xu2NaJh/u8zGQf/Xtn43ck6fzJCO+eodBRmS+beD\nuTLZLIyoUCY2YkPrVj//lzT1yiaP+NBFEsr4IR8+5f5qKHQjU8ykNvAeWzNP0nSn\n5bBgVq8i6wKBgQCRgDs9KjxrDKlwKN2H4VUSj1SA1xJd0XVFcVrTXIyqPqhZp5c6\n/nMRI2FOVcLYaKWhdjmYQ9D/px33PZdeABQWTlie74isQ7hCTl+TXY5X9su8nrZB\nQjGETBfI14XkmUwkrfr9N7d5N5bp8uKTlmTpMwIRxBeRU4qcpGY77/I11QKBgQCc\niIKOFukqmfphbpvxd6cqtYV2hyTuQtpT5RGzvTCR3jM6quWHKWsfIkgidQGChY/C\n3vvJNCx49UTD6vs/CRgB1I6CabPsnxTzAmVpbO7gz3hX1va/TDiA9zQG1zqwuS2q\nnvmRIJ+2K7bBU/mYT87OS6GzQKGSGWh0dFKtnf1WvQKBgFffR7nCnYnwgKYEUbYY\nLmIXR6GtAVoh+t74xMpAesEEVxXuA8dTpwnwzZmh44MgO0POHUdGvwhT21YaR05q\n3SKEnJEL+jZGMA9gKw5aVAljh4YI+rSwwnkOEhZXOMxHjQOJAqGhgMyx5qqQ7WlW\nqNpv7/w4Z/WmDpHr9ky/8s/6\n-----END PRIVATE KEY-----\n",
    "client_email": "comhand@comhand.iam.gserviceaccount.com",
    "client_id": "112551259146708670784",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/comhand%40comhand.iam.gserviceaccount.com"
    }'''
    try:
        phrase = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
        return str(phrase)
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
        return 'google'
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
        return 'google'

