import json

definitions={}

def extract_components(components):
        
    C_schema_representation = f'.structure('
    for element in components:
        C_element_id=None
        C_element_desc=None
        C_element_data_type=None
        C_element_required=None
        C_element_max_length=None
        C_element_min_length=None
        C_element_qualifier_ref=None
        
        C_element_id = element["Id"]
        C_element_desc = element["Desc"]
        try:
            C_element_required = str(element["Required"])
        except KeyError:
            pass
        
        try:
            C_element_data_type = element["DataType"]
        except KeyError:
            pass
        try:
            C_element_min_length = element.get("MinLength")
        except KeyError:
            pass
        try:
            C_element_max_length = element.get("MaxLength")
        except KeyError:
            pass
        try:
            C_element_qualifier_ref=element.get("QualifierRef")
        except KeyError:
            pass

        C_schema_representation += f'new Segment(null,{{id:"{C_element_id}", desc:"{C_element_desc}",Required:{C_element_required}'
        #X_schema_representation += f'new Segment(null,{{id:"{element_id}", desc:"{element_desc}",Required:{element_required},'
        if C_element_data_type is not None:
            C_schema_representation +=f',DataType:"{C_element_data_type}"'
            
        if C_element_min_length is not None and C_element_max_length is not None:
            C_schema_representation += f',Length:[{C_element_min_length},{C_element_max_length}]'
        
            
        if C_element_qualifier_ref is not None:
            C_schema_representation +=f',QualifierRef:"{C_element_qualifier_ref}"'
        C_schema_representation += '}),'
        
    return C_schema_representation+'),'


if __name__ == "__main__":
    with open(r'C:\Users\NHI470\Desktop\Work\X12 Standards\00501\RSSBus_00501.json', 'r') as f:
        data = json.load(f)
        for key , items in data.items():
            if key=="Segments":
                segments=data.get("Segments")
                
                # Generate schema representation for all segments
                for segment_tag, segment_data in segments.items():
                    # if segment_tag=="EC":  
                    #     break
                    #structure = f'new Segment(null,{{tag:"{tag}"}}).structure({structures_string})'
                    schema_representation = f'new Segment(null,{{tag:"{segment_tag}"}}).structure('
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
                        #substructure=f'new Segment(null, {{tag: "{subname}", mandatory: {submandatory}, length: [{submin}, {submax}], ref: "{subref}"}})'

                        schema_representation += f'new Segment(null,{{id:"{element_id}", desc:"{element_desc}",Required:{element_required}'
                        if element_data_type is not None:
                            schema_representation +=f',DataType:"{element_data_type}"'
                            
                        if element_min_length is not None and element_max_length is not None:
                            schema_representation += f',Length:[{element_min_length},{element_max_length}]'

                            
                        if element_qualifier_ref is not None:
                            schema_representation +=f',QualifierRef:"{element_qualifier_ref}"'
                        element_components=None
                        try :
                            element_components=element_data.get("Components")
                            
                        except:
                            pass
                        if element_components is not None:
                            schema_representation += '}'
                            comp_data=extract_components(element_components)
                            schema_representation += ')'
                            schema_representation +=comp_data
                        if element_components is None:
                            schema_representation += '}),'
                    
                        #print(schema_representation)

                    schema_representation += ')'
                    definitions[segment_tag]=schema_representation
    
  
    with open(r'C:\Users\NHI470\Desktop\Work\X12 Standards\Output\index_503.js', 'w') as fp:
            fp.write(f" const Segment = require('./../../../segment').Segment\n\ndefinitions={definitions} \n\n module.exports = definitions")  
