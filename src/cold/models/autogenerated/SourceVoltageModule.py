
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalThermodynamicQuantityModule import ElectrochemicalThermodynamicQuantity



from .CellVoltageModule import CellVoltage



from .VoltageModule import Voltage







class SourceVoltage(ElectrochemicalThermodynamicQuantity, CellVoltage, Voltage):
    """
    Class representing the `SourceVoltage` entity, which inherits from:
    - ElectrochemicalThermodynamicQuantity, CellVoltage, Voltage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5c78b424_087b_4e31_8c91_6422f1be1e86'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SourceVoltage'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SourceVoltage(
    
    class_iri='https://w3id.org/emmo#EMMO_5c78b424_087b_4e31_8c91_6422f1be1e86',
    
    class_name='SourceVoltage',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5c78b424_087b_4e31_8c91_6422f1be1e86',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SourceVoltage',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    