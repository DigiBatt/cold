
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TemperatureCoefficientOfTheOpenCircuitVoltageModule import TemperatureCoefficientOfTheOpenCircuitVoltage







class PositiveElectrodeEntropicChangeCoefficient(TemperatureCoefficientOfTheOpenCircuitVoltage):
    """
    Class representing the `PositiveElectrodeEntropicChangeCoefficient` entity, which inherits from:
    - TemperatureCoefficientOfTheOpenCircuitVoltage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9d558b56_d3b8_429a_a4e2_d2ffab895e42'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PositiveElectrodeEntropicChangeCoefficient'`
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
    obj = PositiveElectrodeEntropicChangeCoefficient(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9d558b56_d3b8_429a_a4e2_d2ffab895e42',
    
    class_name='PositiveElectrodeEntropicChangeCoefficient',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9d558b56_d3b8_429a_a4e2_d2ffab895e42',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PositiveElectrodeEntropicChangeCoefficient',
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
    

    
    

    

    