import json



definitions={}

def extract(segment):
    elements = segment.get('Elements')
    for element in elements:
        print(type(element))
        print(element.get('Id'))



if __name__ == "__main__":
    with open(r'C:\Users\NHI470\Desktop\Work\X12 Standards\00501\RSSBus_00501.json', 'r') as f:
        data = json.load(f)
        for key_1 , items_1 in data.items():
            if key_1=="Segments":
                segments=data.get("Segments")
                for key_2 , items_2 in segments.items():
                    #print(key_2)
                    segment=segments.get(key_2)
                    extract(segment)





















