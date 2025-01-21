
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InterfacialRegionModule import InterfacialRegion







class Interphase(InterfacialRegion):
    """
    Class representing the `Interphase` entity, which inherits from:
    - InterfacialRegion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_54e0c2bd_1bb2_4f9c_9b55_5b6cc34651ec'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Interphase'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `figure` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `figure`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Interphase(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_54e0c2bd_1bb2_4f9c_9b55_5b6cc34651ec',
    
    class_name='Interphase',
    
    iupacReference="example_value",
    
    figure="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_54e0c2bd_1bb2_4f9c_9b55_5b6cc34651ec',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Interphase',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    figure: Optional[str] = Field(
        None,
        alias="figure"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    