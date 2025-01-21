
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InterfacialRegionModule import InterfacialRegion







class DoubleLayer(InterfacialRegion):
    """
    Class representing the `DoubleLayer` entity, which inherits from:
    - InterfacialRegion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2b50cdac_581f_48b9_87ca_bad5138ab58d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DoubleLayer'`
        - **Alias**: `class_name`
    
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
    obj = DoubleLayer(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2b50cdac_581f_48b9_87ca_bad5138ab58d',
    
    class_name='DoubleLayer',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2b50cdac_581f_48b9_87ca_bad5138ab58d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DoubleLayer',
        alias="class_name"
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
    

    
    

    

    