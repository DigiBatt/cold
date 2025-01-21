
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalCellModule import ElectrochemicalCell



from .HolisticArrangementModule import HolisticArrangement





from .ElectrolyteModule import Electrolyte



from .ElectrodeModule import Electrode





class ElectrochemicalHalfCell(ElectrochemicalCell, HolisticArrangement):
    """
    Class representing the `ElectrochemicalHalfCell` entity, which inherits from:
    - ElectrochemicalCell, HolisticArrangement

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9da958fc_f76d_4654_8a78_99b5f98c118c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalHalfCell'`
        - **Alias**: `class_name`
    
    - `hasElectrolyte` (`Optional[Electrolyte]`): 
        - **Default Value**: `None`
        - **Alias**: `hasElectrolyte`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasElectrode` (`Optional[Electrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasElectrode`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalHalfCell(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9da958fc_f76d_4654_8a78_99b5f98c118c',
    
    class_name='ElectrochemicalHalfCell',
    
    hasElectrolyte="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    hasElectrode="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9da958fc_f76d_4654_8a78_99b5f98c118c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalHalfCell',
        alias="class_name"
    )
    
    hasElectrolyte: Optional[Electrolyte] = Field(
        None,
        alias="hasElectrolyte"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasElectrode: Optional[Electrode] = Field(
        None,
        alias="hasElectrode"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    @validator("hasElectrolyte", pre=True, always=True)
    def validate_hasElectrolyte(cls, value):
        if value is not None and not isinstance(value, Electrolyte):
            raise ValueError(f"Field 'hasElectrolyte' must be an instance of 'Electrolyte' or its subclass.")
        return value
    
    @validator("hasElectrode", pre=True, always=True)
    def validate_hasElectrode(cls, value):
        if value is not None and not isinstance(value, Electrode):
            raise ValueError(f"Field 'hasElectrode' must be an instance of 'Electrode' or its subclass.")
        return value
    
    

    

    