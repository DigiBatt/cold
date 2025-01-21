
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalModule import Electrochemical



from .ElectrochemicalTestingProcedureModule import ElectrochemicalTestingProcedure







class PseudoOpenCircuitVoltageTest(Electrochemical, ElectrochemicalTestingProcedure):
    """
    Class representing the `PseudoOpenCircuitVoltageTest` entity, which inherits from:
    - Electrochemical, ElectrochemicalTestingProcedure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_00244072_8d24_4e34_9f6a_c7b2b132b2c8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PseudoOpenCircuitVoltageTest'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PseudoOpenCircuitVoltageTest(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_00244072_8d24_4e34_9f6a_c7b2b132b2c8',
    
    class_name='PseudoOpenCircuitVoltageTest',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_00244072_8d24_4e34_9f6a_c7b2b132b2c8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PseudoOpenCircuitVoltageTest',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    