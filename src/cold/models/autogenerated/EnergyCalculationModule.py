
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WholeModule import Whole



from .ProcessModule import Process



from .MeasurementDataPostProcessingModule import MeasurementDataPostProcessing







class EnergyCalculation(Whole, Process, MeasurementDataPostProcessing):
    """
    Class representing the `EnergyCalculation` entity, which inherits from:
    - Whole, Process, MeasurementDataPostProcessing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cbb95634_450c_4332_980c_d37baadd7619'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EnergyCalculation'`
        - **Alias**: `class_name`
    
    - `hasOutput` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasOutput`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasInput` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasInput`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EnergyCalculation(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cbb95634_450c_4332_980c_d37baadd7619',
    
    class_name='EnergyCalculation',
    
    hasOutput="example_value",
    
    elucidation="example_value",
    
    hasInput="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cbb95634_450c_4332_980c_d37baadd7619',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EnergyCalculation',
        alias="class_name"
    )
    
    hasOutput: Optional[str] = Field(
        None,
        alias="hasOutput"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasInput: Optional[str] = Field(
        None,
        alias="hasInput"
    )
    

    
    

    

    