
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThermodynamicalQuantityModule import ThermodynamicalQuantity



from .RatioQuantityModule import RatioQuantity







class ThermodynamicEfficiency(ThermodynamicalQuantity, RatioQuantity):
    """
    Class representing the `ThermodynamicEfficiency` entity, which inherits from:
    - ThermodynamicalQuantity, RatioQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e37ec2b9_aed3_4549_ad25_5f78d31cac06'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThermodynamicEfficiency'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ThermodynamicEfficiency(
    
    class_iri='https://w3id.org/emmo#EMMO_e37ec2b9_aed3_4549_ad25_5f78d31cac06',
    
    class_name='ThermodynamicEfficiency',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e37ec2b9_aed3_4549_ad25_5f78d31cac06',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThermodynamicEfficiency',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    