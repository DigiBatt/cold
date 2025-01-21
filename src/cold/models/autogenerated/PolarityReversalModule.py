
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IntentionalProcessModule import IntentionalProcess







class PolarityReversal(IntentionalProcess):
    """
    Class representing the `PolarityReversal` entity, which inherits from:
    - IntentionalProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_83d2c2d4_ffa9_42f4_9264_a0c59c657607'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PolarityReversal'`
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
    obj = PolarityReversal(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_83d2c2d4_ffa9_42f4_9264_a0c59c657607',
    
    class_name='PolarityReversal',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_83d2c2d4_ffa9_42f4_9264_a0c59c657607',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PolarityReversal',
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
    

    
    

    

    