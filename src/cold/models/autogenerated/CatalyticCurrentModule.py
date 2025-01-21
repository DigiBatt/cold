
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FaradaicCurrentModule import FaradaicCurrent







class CatalyticCurrent(FaradaicCurrent):
    """
    Class representing the `CatalyticCurrent` entity, which inherits from:
    - FaradaicCurrent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c55bcb85_b7b8_4e67_8a78_9a42fe25b6cf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CatalyticCurrent'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CatalyticCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c55bcb85_b7b8_4e67_8a78_9a42fe25b6cf',
    
    class_name='CatalyticCurrent',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c55bcb85_b7b8_4e67_8a78_9a42fe25b6cf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CatalyticCurrent',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    