
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SystemUnitModule import SystemUnit








class CGSUnit(SystemUnit):
    """
    Class representing the `CGSUnit` entity, which inherits from:
    - SystemUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_52e4cb25_da39_45e2_a6db_063ec5730499'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CGSUnit'`
        - **Alias**: `class_name`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CGSUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_52e4cb25_da39_45e2_a6db_063ec5730499',
    
    class_name='CGSUnit',
    
    wikipediaReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#EMMO_52e4cb25_da39_45e2_a6db_063ec5730499',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'CGSUnit',
        
        alias="class_name"
    )
    
    wikipediaReference: Optional[str] = Field(
        
            None,
        
        alias="wikipediaReference"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    


    
    

    

    