
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VoltageModule import Voltage







class NominalVoltage(Voltage):
    """
    Class representing the `NominalVoltage` entity, which inherits from:
    - Voltage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_639b844a_e801_436b_985d_28926129ead6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NominalVoltage'`
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
    obj = NominalVoltage(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_639b844a_e801_436b_985d_28926129ead6',
    
    class_name='NominalVoltage',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_639b844a_e801_436b_985d_28926129ead6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NominalVoltage',
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
    

    
    

    

    