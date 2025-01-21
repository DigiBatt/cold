
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FaradaicCurrentModule import FaradaicCurrent







class DiffusionCurrent(FaradaicCurrent):
    """
    Class representing the `DiffusionCurrent` entity, which inherits from:
    - FaradaicCurrent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_17626b8e_dfce_4d3a_ae6c_5a7215d43a90'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DiffusionCurrent'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DiffusionCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_17626b8e_dfce_4d3a_ae6c_5a7215d43a90',
    
    class_name='DiffusionCurrent',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_17626b8e_dfce_4d3a_ae6c_5a7215d43a90',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DiffusionCurrent',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    