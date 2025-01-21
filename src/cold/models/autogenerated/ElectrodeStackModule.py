
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AssembledModule import Assembled







class ElectrodeStack(Assembled):
    """
    Class representing the `ElectrodeStack` entity, which inherits from:
    - Assembled

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_27662d03_1bcf_4393_a239_32e31b760839'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrodeStack'`
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
    obj = ElectrodeStack(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_27662d03_1bcf_4393_a239_32e31b760839',
    
    class_name='ElectrodeStack',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_27662d03_1bcf_4393_a239_32e31b760839',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrodeStack',
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
    

    
    

    

    