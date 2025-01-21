
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChargingModule import Charging







class EqualizationCharge(Charging):
    """
    Class representing the `EqualizationCharge` entity, which inherits from:
    - Charging

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_990d19b8_672a_4219_a2b3_0a25bfa13f69'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EqualizationCharge'`
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
    obj = EqualizationCharge(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_990d19b8_672a_4219_a2b3_0a25bfa13f69',
    
    class_name='EqualizationCharge',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_990d19b8_672a_4219_a2b3_0a25bfa13f69',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EqualizationCharge',
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
    

    
    

    

    