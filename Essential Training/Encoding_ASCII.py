def decode_tuples(encodedList):
    """
    Decodes a list of tuples into a string.
    Args: encodedList (list of tuples): Each tuple contains a character and an integer.
    Returns: str: Decoded string by repeating each character based on the integer value.
    """
    decoded_string = []
    for key, value in encodedList:
        decoded_string.append(key * value)
    return ''.join(decoded_string)

def encode_string(stringVal):
    """
    Encodes a string into a list of tuples where each tuple contains a character
    and the number of its consecutive occurrences.
    Args: stringVal (str): The input string to encode.
    Returns: list: A list of tuples with characters and their counts.
    """
    encoded_string = []
    prev_char = None
    count = 1

    for char in stringVal:
        if char != prev_char:
            if prev_char is not None:
                encoded_string.append((prev_char, count))
            count = 1
            prev_char = char
        else:
            count += 1

    encoded_string.append((prev_char, count))

    return encoded_string

if __name__ == "__main__":
    art = '''

                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                 

'''
    # Pass 'art' to encode_string
    encoded_result = encode_string(art)
    print("Encoded Result:", encoded_result)

    # Pass the encoded result to decode_tuples
    decoded_result = decode_tuples(encoded_result)
    print("Decoded Result:", decoded_result)