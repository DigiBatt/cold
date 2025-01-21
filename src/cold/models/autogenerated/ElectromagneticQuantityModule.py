
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISO80000CategorisedModule import ISO80000Categorised







class ElectromagneticQuantity(ISO80000Categorised):
    """
    Class representing the `ElectromagneticQuantity` entity, which inherits from:
    - ISO80000Categorised

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_af794e9d_dc7d_4756_83e1_2cd0e2ec864e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectromagneticQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectromagneticQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_af794e9d_dc7d_4756_83e1_2cd0e2ec864e',
    
    class_name='ElectromagneticQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_af794e9d_dc7d_4756_83e1_2cd0e2ec864e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectromagneticQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    