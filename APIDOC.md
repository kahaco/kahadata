# API Endpoint 

## Get list of resources
    <server>/resources/<district>

    Eg:
    http://api.kaha.co/resources/kathmandu
    http://api.kaha.co/resources/all
    
*NOTE* Return list of resources for matching district.


    <server>/resources/<district>?for=need
*NOTE* Return list of resources matching the district and of type 'Need'

    <server>/resources/<district>/<resource_type>
    <server>/resources/<district>/<resource_type>,<resource_type>

    Eg: 
    http://api.kaha.co/kathmandu/food,blood

*NOTE* Return list of resources for matching district and resource types

    <server>/resource/<uuid>
*NOTE* Return a resource for the uuid
