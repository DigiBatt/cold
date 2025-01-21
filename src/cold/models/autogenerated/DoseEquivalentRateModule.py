
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AbsorbedDoseRateModule import AbsorbedDoseRate







class DoseEquivalentRate(AbsorbedDoseRate):
    """
    Class representing the `DoseEquivalentRate` entity, which inherits from:
    - AbsorbedDoseRate

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_01e4191d_03ba_4107_a307_1c09c0e6a7d2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DoseEquivalentRate'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DoseEquivalentRate(
    
    class_iri='https://w3id.org/emmo#EMMO_01e4191d_03ba_4107_a307_1c09c0e6a7d2',
    
    class_name='DoseEquivalentRate',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_01e4191d_03ba_4107_a307_1c09c0e6a7d2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DoseEquivalentRate',
        alias="class_name"
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    