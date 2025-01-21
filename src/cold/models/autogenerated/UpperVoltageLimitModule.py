
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VoltageLimitModule import VoltageLimit







class UpperVoltageLimit(VoltageLimit):
    """
    Class representing the `UpperVoltageLimit` entity, which inherits from:
    - VoltageLimit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6dcd5baf_58cd_43f5_a692_51508e036c88'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'UpperVoltageLimit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = UpperVoltageLimit(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6dcd5baf_58cd_43f5_a692_51508e036c88',
    
    class_name='UpperVoltageLimit',
    
    elucidation="example_value",
    
    comment="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6dcd5baf_58cd_43f5_a692_51508e036c88',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'UpperVoltageLimit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    