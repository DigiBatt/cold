
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CrystallineMaterialModule import CrystallineMaterial







class Crystal(CrystallineMaterial):
    """
    Class representing the `Crystal` entity, which inherits from:
    - CrystallineMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0bb3b434_73aa_428f_b4e8_2a2468648e19'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Crystal'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Crystal(
    
    class_iri='https://w3id.org/emmo#EMMO_0bb3b434_73aa_428f_b4e8_2a2468648e19',
    
    class_name='Crystal',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0bb3b434_73aa_428f_b4e8_2a2468648e19',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Crystal',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    