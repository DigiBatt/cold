
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AssembledModule import Assembled







class ParallelConnection(Assembled):
    """
    Class representing the `ParallelConnection` entity, which inherits from:
    - Assembled

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_efc4f7ab_850d_443c_a17f_184983021f96'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ParallelConnection'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ParallelConnection(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_efc4f7ab_850d_443c_a17f_184983021f96',
    
    class_name='ParallelConnection',
    
    wikidataReference="example_value",
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_efc4f7ab_850d_443c_a17f_184983021f96',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ParallelConnection',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    