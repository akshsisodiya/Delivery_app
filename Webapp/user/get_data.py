class CardView:
    def __init__(self,title,img,link,description):
        self.title=title
        self.img=img
        self.link=link
        self.description=description

def index_data():
    profile = CardView('Profile', 'aksh004.jpg', 'profile', 'Goto your profile')
    send_p = CardView('Send Parcel', 'send.jpg', 'send_parcel', 'Quick proccess to send your parcel')
    request_p = CardView('Request Parcel', 'request.jpg', 'requset_parcel', 'Request something from your friendlist')
    track_d = CardView('Track Delivery', 'tracking.jpg', 'track_delivery', 'Track current location of your parcels')
    return [send_p,request_p,track_d,profile]
