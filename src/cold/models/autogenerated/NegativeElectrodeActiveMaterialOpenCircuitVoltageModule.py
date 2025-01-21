
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SourceVoltageModule import SourceVoltage



from .OpenCircuitVoltageModule import OpenCircuitVoltage







class NegativeElectrodeActiveMaterialOpenCircuitVoltage(SourceVoltage, OpenCircuitVoltage):
    """
    Class representing the `NegativeElectrodeActiveMaterialOpenCircuitVoltage` entity, which inherits from:
    - SourceVoltage, OpenCircuitVoltage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0e2f4fe6_570a_4d13_81e9_de1d4f9987af'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NegativeElectrodeActiveMaterialOpenCircuitVoltage'`
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
    obj = NegativeElectrodeActiveMaterialOpenCircuitVoltage(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0e2f4fe6_570a_4d13_81e9_de1d4f9987af',
    
    class_name='NegativeElectrodeActiveMaterialOpenCircuitVoltage',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0e2f4fe6_570a_4d13_81e9_de1d4f9987af',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NegativeElectrodeActiveMaterialOpenCircuitVoltage',
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
    

    
    

    

    