
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HolisticArrangementModule import HolisticArrangement





from .ElectrolyteModule import Electrolyte



from .ReferenceElectrodeModule import ReferenceElectrode



from .PositiveElectrodeModule import PositiveElectrode



from .NegativeElectrodeModule import NegativeElectrode



from .ElectrodeModule import Electrode





class ElectrochemicalCell(HolisticArrangement):
    """
    Class representing the `ElectrochemicalCell` entity, which inherits from:
    - HolisticArrangement

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6f2c88c9_5c04_4953_a298_032cc3ab9b77'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalCell'`
        - **Alias**: `class_name`
    
    - `hasANSICode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasANSICode`
    
    - `hasElectrolyte` (`Optional[Electrolyte]`): 
        - **Default Value**: `None`
        - **Alias**: `hasElectrolyte`
    
    - `figure` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `figure`
    
    - `hasReferenceElectrode` (`Optional[ReferenceElectrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasReferenceElectrode`
    
    - `hasWorkingElectrode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasWorkingElectrode`
    
    - `hasCounterElectrode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasCounterElectrode`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `hasPositiveElectrode` (`Optional[PositiveElectrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPositiveElectrode`
    
    - `hasNegativeElectrode` (`Optional[NegativeElectrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasNegativeElectrode`
    
    - `hasIECCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasIECCode`
    
    - `dbpediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `dbpediaReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `hasElectrode` (`Optional[Electrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasElectrode`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `hasPositiveElectrode` (`Optional[Electrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPositiveElectrode`
    
    - `hasNegativeElectrode` (`Optional[Electrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasNegativeElectrode`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalCell(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6f2c88c9_5c04_4953_a298_032cc3ab9b77',
    
    class_name='ElectrochemicalCell',
    
    hasANSICode="example_value",
    
    hasElectrolyte="example_value",
    
    figure="example_value",
    
    hasReferenceElectrode="example_value",
    
    hasWorkingElectrode="example_value",
    
    hasCounterElectrode="example_value",
    
    wikidataReference="example_value",
    
    hasPositiveElectrode="example_value",
    
    hasNegativeElectrode="example_value",
    
    hasIECCode="example_value",
    
    dbpediaReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    IEVReference="example_value",
    
    hasElectrode="example_value",
    
    wikipediaReference="example_value",
    
    hasPositiveElectrode=None,
    
    hasNegativeElectrode=None,
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6f2c88c9_5c04_4953_a298_032cc3ab9b77',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalCell',
        alias="class_name"
    )
    
    hasANSICode: Optional[str] = Field(
        None,
        alias="hasANSICode"
    )
    
    hasElectrolyte: Optional[Electrolyte] = Field(
        None,
        alias="hasElectrolyte"
    )
    
    figure: Optional[str] = Field(
        None,
        alias="figure"
    )
    
    hasReferenceElectrode: Optional[ReferenceElectrode] = Field(
        None,
        alias="hasReferenceElectrode"
    )
    
    hasWorkingElectrode: Optional[str] = Field(
        None,
        alias="hasWorkingElectrode"
    )
    
    hasCounterElectrode: Optional[str] = Field(
        None,
        alias="hasCounterElectrode"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    hasPositiveElectrode: Optional[PositiveElectrode] = Field(
        None,
        alias="hasPositiveElectrode"
    )
    
    hasNegativeElectrode: Optional[NegativeElectrode] = Field(
        None,
        alias="hasNegativeElectrode"
    )
    
    hasIECCode: Optional[str] = Field(
        None,
        alias="hasIECCode"
    )
    
    dbpediaReference: Optional[str] = Field(
        None,
        alias="dbpediaReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    hasElectrode: Optional[Electrode] = Field(
        None,
        alias="hasElectrode"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    
    hasPositiveElectrode: Optional[Electrode] = Field(
        None,
        alias="hasPositiveElectrode"
    )
    
    hasNegativeElectrode: Optional[Electrode] = Field(
        None,
        alias="hasNegativeElectrode"
    )
    

    
    @validator("hasElectrolyte", pre=True, always=True)
    def validate_hasElectrolyte(cls, value):
        if value is not None and not isinstance(value, Electrolyte):
            raise ValueError(f"Field 'hasElectrolyte' must be an instance of 'Electrolyte' or its subclass.")
        return value
    
    @validator("hasReferenceElectrode", pre=True, always=True)
    def validate_hasReferenceElectrode(cls, value):
        if value is not None and not isinstance(value, ReferenceElectrode):
            raise ValueError(f"Field 'hasReferenceElectrode' must be an instance of 'ReferenceElectrode' or its subclass.")
        return value
    
    @validator("hasPositiveElectrode", pre=True, always=True)
    def validate_hasPositiveElectrode(cls, value):
        if value is not None and not isinstance(value, PositiveElectrode):
            raise ValueError(f"Field 'hasPositiveElectrode' must be an instance of 'PositiveElectrode' or its subclass.")
        return value
    
    @validator("hasNegativeElectrode", pre=True, always=True)
    def validate_hasNegativeElectrode(cls, value):
        if value is not None and not isinstance(value, NegativeElectrode):
            raise ValueError(f"Field 'hasNegativeElectrode' must be an instance of 'NegativeElectrode' or its subclass.")
        return value
    
    @validator("hasElectrode", pre=True, always=True)
    def validate_hasElectrode(cls, value):
        if value is not None and not isinstance(value, Electrode):
            raise ValueError(f"Field 'hasElectrode' must be an instance of 'Electrode' or its subclass.")
        return value
    
    @validator("hasPositiveElectrode", pre=True, always=True)
    def validate_hasPositiveElectrode(cls, value):
        if value is not None and not isinstance(value, Electrode):
            raise ValueError(f"Field 'hasPositiveElectrode' must be an instance of 'Electrode' or its subclass.")
        return value
    
    @validator("hasNegativeElectrode", pre=True, always=True)
    def validate_hasNegativeElectrode(cls, value):
        if value is not None and not isinstance(value, Electrode):
            raise ValueError(f"Field 'hasNegativeElectrode' must be an instance of 'Electrode' or its subclass.")
        return value
    
    

    

    