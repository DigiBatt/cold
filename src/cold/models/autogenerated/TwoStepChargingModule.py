
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SerialWorkflowModule import SerialWorkflow



from .ChargingModule import Charging







class TwoStepCharging(SerialWorkflow, Charging):
    """
    Class representing the `TwoStepCharging` entity, which inherits from:
    - SerialWorkflow, Charging

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_aac51107_dbe5_4e63_b08a_9d6cf88f4b69'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TwoStepCharging'`
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
    obj = TwoStepCharging(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_aac51107_dbe5_4e63_b08a_9d6cf88f4b69',
    
    class_name='TwoStepCharging',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_aac51107_dbe5_4e63_b08a_9d6cf88f4b69',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TwoStepCharging',
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
    

    
    

    

    