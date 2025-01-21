
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NonTemporalRoleModule import NonTemporalRole







class Interface(NonTemporalRole):
    """
    Class representing the `Interface` entity, which inherits from:
    - NonTemporalRole

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_94d9d5e2_9e9b_4eb7_b3ce_f3d658b7ae64'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Interface'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `figure` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `figure`
    
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
    obj = Interface(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_94d9d5e2_9e9b_4eb7_b3ce_f3d658b7ae64',
    
    class_name='Interface',
    
    iupacReference="example_value",
    
    figure="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_94d9d5e2_9e9b_4eb7_b3ce_f3d658b7ae64',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Interface',
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
    

    
    

    

    