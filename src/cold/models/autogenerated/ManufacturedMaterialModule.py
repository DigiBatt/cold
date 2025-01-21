
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialModule import Material



from .ManufacturedProductModule import ManufacturedProduct







class ManufacturedMaterial(Material, ManufacturedProduct):
    """
    Class representing the `ManufacturedMaterial` entity, which inherits from:
    - Material, ManufacturedProduct

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ec7464a9_d99d_45f8_965b_4e9230ea8356'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ManufacturedMaterial'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ManufacturedMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_ec7464a9_d99d_45f8_965b_4e9230ea8356',
    
    class_name='ManufacturedMaterial',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ec7464a9_d99d_45f8_965b_4e9230ea8356',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ManufacturedMaterial',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    