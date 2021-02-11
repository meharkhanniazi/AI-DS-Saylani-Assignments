dic = {}
def make_album(artistName, albumTitle, noOfSongs = None):
    dic.update({artistName:albumTitle})
    if noOfSongs:
        dic.update({"Number of Songs":noOfSongs})
    return dic