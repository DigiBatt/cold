
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TemperatureCoefficientOfTheOpenCircuitVoltageModule import TemperatureCoefficientOfTheOpenCircuitVoltage







class NegativeElectrodeEntropicChangeCoefficient(TemperatureCoefficientOfTheOpenCircuitVoltage):
    """
    Class representing the `NegativeElectrodeEntropicChangeCoefficient` entity, which inherits from:
    - TemperatureCoefficientOfTheOpenCircuitVoltage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_eac57b09_5cc9_41d7_b2c8_40218d7fd47c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NegativeElectrodeEntropicChangeCoefficient'`
        - **Alias**: `class_name`
    
    - `cidemodKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `cidemodKey`
    
    - `bpxKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `bpxKey`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NegativeElectrodeEntropicChangeCoefficient(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_eac57b09_5cc9_41d7_b2c8_40218d7fd47c',
    
    class_name='NegativeElectrodeEntropicChangeCoefficient',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_eac57b09_5cc9_41d7_b2c8_40218d7fd47c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NegativeElectrodeEntropicChangeCoefficient',
        alias="class_name"
    )
    
    cidemodKey: Optional[str] = Field(
        None,
        alias="cidemodKey"
    )
    
    bpxKey: Optional[str] = Field(
        None,
        alias="bpxKey"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    