
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TimeSeriesElectricalDataSetModule import TimeSeriesElectricalDataSet







class PseudoOpenCircuitVoltageData(TimeSeriesElectricalDataSet):
    """
    Class representing the `PseudoOpenCircuitVoltageData` entity, which inherits from:
    - TimeSeriesElectricalDataSet

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a49d9cd1_bec8_4d1d_9657_d47983e9135d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PseudoOpenCircuitVoltageData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PseudoOpenCircuitVoltageData(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a49d9cd1_bec8_4d1d_9657_d47983e9135d',
    
    class_name='PseudoOpenCircuitVoltageData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a49d9cd1_bec8_4d1d_9657_d47983e9135d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PseudoOpenCircuitVoltageData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    