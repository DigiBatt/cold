
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AssembledModule import Assembled







class ParallelSeriesConnection(Assembled):
    """
    Class representing the `ParallelSeriesConnection` entity, which inherits from:
    - Assembled

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d5da9948_e95b_4f12_a2d2_10a48f390c52'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ParallelSeriesConnection'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ParallelSeriesConnection(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d5da9948_e95b_4f12_a2d2_10a48f390c52',
    
    class_name='ParallelSeriesConnection',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d5da9948_e95b_4f12_a2d2_10a48f390c52',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ParallelSeriesConnection',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    