
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TimeSeriesElectricalDataSetModule import TimeSeriesElectricalDataSet







class GalvanostaticIntermittentTitrationTechniqueData(TimeSeriesElectricalDataSet):
    """
    Class representing the `GalvanostaticIntermittentTitrationTechniqueData` entity, which inherits from:
    - TimeSeriesElectricalDataSet

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ac2ffdd9_09cf_42a7_ba6a_1c6968e9a8a5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GalvanostaticIntermittentTitrationTechniqueData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GalvanostaticIntermittentTitrationTechniqueData(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ac2ffdd9_09cf_42a7_ba6a_1c6968e9a8a5',
    
    class_name='GalvanostaticIntermittentTitrationTechniqueData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ac2ffdd9_09cf_42a7_ba6a_1c6968e9a8a5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GalvanostaticIntermittentTitrationTechniqueData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    