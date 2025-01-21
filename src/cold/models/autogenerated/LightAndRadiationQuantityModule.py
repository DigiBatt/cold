
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISO80000CategorisedModule import ISO80000Categorised







class LightAndRadiationQuantity(ISO80000Categorised):
    """
    Class representing the `LightAndRadiationQuantity` entity, which inherits from:
    - ISO80000Categorised

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ec1aa2cd_74eb_4506_81d1_901a3124aaba'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LightAndRadiationQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LightAndRadiationQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_ec1aa2cd_74eb_4506_81d1_901a3124aaba',
    
    class_name='LightAndRadiationQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ec1aa2cd_74eb_4506_81d1_901a3124aaba',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LightAndRadiationQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    