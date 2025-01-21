
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPhenomenonModule import ElectrochemicalPhenomenon







class Electrocapillarity(ElectrochemicalPhenomenon):
    """
    Class representing the `Electrocapillarity` entity, which inherits from:
    - ElectrochemicalPhenomenon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5cb5548f_f774_4668_ad02_f0742581f2f1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Electrocapillarity'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Electrocapillarity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5cb5548f_f774_4668_ad02_f0742581f2f1',
    
    class_name='Electrocapillarity',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5cb5548f_f774_4668_ad02_f0742581f2f1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Electrocapillarity',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    