
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ProductModule import Product



from .IntentionalProcessModule import IntentionalProcess







class Service(Product, IntentionalProcess):
    """
    Class representing the `Service` entity, which inherits from:
    - Product, IntentionalProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_127594de_4802_4ad6_b09d_d05b340394dd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Service'`
        - **Alias**: `class_name`
    
    - `ISO9000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO9000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Service(
    
    class_iri='https://w3id.org/emmo#EMMO_127594de_4802_4ad6_b09d_d05b340394dd',
    
    class_name='Service',
    
    ISO9000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_127594de_4802_4ad6_b09d_d05b340394dd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Service',
        alias="class_name"
    )
    
    ISO9000Reference: Optional[str] = Field(
        None,
        alias="ISO9000Reference"
    )
    

    
    

    

    