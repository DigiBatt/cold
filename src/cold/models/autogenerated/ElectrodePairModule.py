
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AssembledModule import Assembled







class ElectrodePair(Assembled):
    """
    Class representing the `ElectrodePair` entity, which inherits from:
    - Assembled

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d907805f_678b_4ab6_8b56_59631684f84b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrodePair'`
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
    obj = ElectrodePair(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d907805f_678b_4ab6_8b56_59631684f84b',
    
    class_name='ElectrodePair',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d907805f_678b_4ab6_8b56_59631684f84b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrodePair',
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
    

    
    

    

    