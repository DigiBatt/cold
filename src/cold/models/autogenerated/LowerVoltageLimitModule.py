
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VoltageLimitModule import VoltageLimit







class LowerVoltageLimit(VoltageLimit):
    """
    Class representing the `LowerVoltageLimit` entity, which inherits from:
    - VoltageLimit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_534dd59c_904c_45d9_8550_ae9d2eb6bbc9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LowerVoltageLimit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LowerVoltageLimit(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_534dd59c_904c_45d9_8550_ae9d2eb6bbc9',
    
    class_name='LowerVoltageLimit',
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_534dd59c_904c_45d9_8550_ae9d2eb6bbc9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LowerVoltageLimit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    