import json

definitions={}


# Define a function to create an element with specified attributes



if __name__ == "__main__":
    with open(r'C:\Users\NHI470\Desktop\Work\X12 Standards\00501\RSSBus_00501.json', 'r') as f:
        data = json.load(f)
        for key , items in data.items():
            if key=="Segments":
                segments=data.get("Segments")
                
                # Generate schema representation for all segments
                for segment_tag, segment_data in segments.items():
                    print(segment_tag)
                    schema_representation = f'Segment(tag="{segment_tag}").structure('
                    for element_data in segment_data["Elements"]:
                        element_id=None
                        element_desc=None
                        element_data_type=None
                        element_required=None
                        element_max_length=None
                        element_min_length=None
                        element_qualifier_ref=None
                        
                        element_id = element_data["Id"]
                        element_desc = element_data["Desc"]
                        
                        try:
                            element_required = str(element_data["Required"])
                        except KeyError:
                            pass
                        try:
                            element_data_type = element_data["DataType"]
                        except KeyError:
                            pass
                        try:
                            element_min_length = element_data.get("MinLength")
                        except KeyError:
                            pass
                        try:
                            element_max_length = element_data.get("MaxLength")
                        except KeyError:
                            pass
                        try:
                            element_qualifier_ref=element_data.get("QualifierRef")
                        except KeyError:
                            pass

                        schema_representation += f'Segment(id="{element_id}", desc="{element_desc}",Required={element_required},'
                        if element_data_type is not None:
                            schema_representation +=f'DataType="{element_data_type}",'
                            
                        if element_min_length is not None:
                            schema_representation += f'MinLength={element_min_length},'
                        
                        if element_max_length is not None:
                            schema_representation += f'MaxLength={element_max_length},'
                            
                        if element_qualifier_ref is not None:
                            schema_representation +=f'QualifierRef="{element_qualifier_ref}"'
                        
                        schema_representation += '),'

                    schema_representation += ')'
                    definitions[segment_tag]=schema_representation
    
  
    with open(r'C:\Users\NHI470\Desktop\Work\X12 Standards\Output\index_502.py', 'w') as fp:
            fp.write(f"from Segment import Segment \n\ndefinitions={definitions}")  
