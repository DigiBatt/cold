
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActiveElectrodeModule import ActiveElectrode



from .ElectrodeModule import Electrode





from .CurrentCollectorModule import CurrentCollector



from .CoatingModule import Coating





class CoatedElectrode(ActiveElectrode, Electrode):
    """
    Class representing the `CoatedElectrode` entity, which inherits from:
    - ActiveElectrode, Electrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_92147e31_d015_4889_a092_04fbab033f15'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CoatedElectrode'`
        - **Alias**: `class_name`
    
    - `hasCurrentCollector` (`Optional[CurrentCollector]`): 
        - **Default Value**: `None`
        - **Alias**: `hasCurrentCollector`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `hasCoating` (`Optional[Coating]`): 
        - **Default Value**: `None`
        - **Alias**: `hasCoating`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CoatedElectrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_92147e31_d015_4889_a092_04fbab033f15',
    
    class_name='CoatedElectrode',
    
    hasCurrentCollector="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    hasCoating="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_92147e31_d015_4889_a092_04fbab033f15',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CoatedElectrode',
        alias="class_name"
    )
    
    hasCurrentCollector: Optional[CurrentCollector] = Field(
        None,
        alias="hasCurrentCollector"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    hasCoating: Optional[Coating] = Field(
        None,
        alias="hasCoating"
    )
    

    
    @validator("hasCurrentCollector", pre=True, always=True)
    def validate_hasCurrentCollector(cls, value):
        if value is not None and not isinstance(value, CurrentCollector):
            raise ValueError(f"Field 'hasCurrentCollector' must be an instance of 'CurrentCollector' or its subclass.")
        return value
    
    @validator("hasCoating", pre=True, always=True)
    def validate_hasCoating(cls, value):
        if value is not None and not isinstance(value, Coating):
            raise ValueError(f"Field 'hasCoating' must be an instance of 'Coating' or its subclass.")
        return value
    
    

    

    