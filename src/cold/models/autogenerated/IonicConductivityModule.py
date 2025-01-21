
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricConductivityModule import ElectricConductivity



from .ElectrochemicalTransportQuantityModule import ElectrochemicalTransportQuantity







class IonicConductivity(ElectricConductivity, ElectrochemicalTransportQuantity):
    """
    Class representing the `IonicConductivity` entity, which inherits from:
    - ElectricConductivity, ElectrochemicalTransportQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_25dabdc2_68bf_4a38_8cbe_11be017358bc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IonicConductivity'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IonicConductivity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_25dabdc2_68bf_4a38_8cbe_11be017358bc',
    
    class_name='IonicConductivity',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_25dabdc2_68bf_4a38_8cbe_11be017358bc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IonicConductivity',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    