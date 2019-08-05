



# Ram on the esp8266 is limited, so we remove all formating as spaces take up ram.
# For me once I had the css how I wanted, I went through and removed all formatting that I did not need.

def standard():
  standard_css ="""html{font-family:Helvetica;display:inline-block;margin:0px auto;text-align:center;background-color:lightgrey;}h1{color:#ffffff;font-size:40px;}p{font-size:1.5rem;color:#ffffff;}.button{display:inline-block;background-color:#676767;border:none;border-radius:8px;color:white;padding:16px40px;text-decoration:none;font-size:24px;margin:2px;cursor:pointer;outline:none;width:100px;}.button:active{background-color:#616161;box-shadow:15px#666;transform:translateY(2px);}#main_div{width:350px;height:350px;margin:auto;margin-top:30px;border-radius:8px;border:5px solid grey;background-color:darkgrey;}::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{-webkit-appearance:none;margin:0;}"""
  return standard_css








