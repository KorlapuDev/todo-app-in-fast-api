from responses import responses


def get_response(response_num: str, custom_msg:str = None, data_to_send:dict = None) -> dict:
    x = responses[response_num]
    if(custom_msg):
        x["message"] = custom_msg
    if(data_to_send):
        x["data"] = data_to_send
    return x
    
